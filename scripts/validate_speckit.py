#!/usr/bin/env python3
"""
Validate speckit from GitHub Issue and extract metadata.
"""
import os
import sys
import json
import re
import requests
from typing import Dict, Optional, Tuple


def parse_issue_body(body: str) -> Dict:
    """Extract information from Issue body."""
    # Extract repository URL
    repo_match = re.search(r'https://github\.com/([^/\s]+)/([^/\s\)]+)', body)
    if not repo_match:
        raise ValueError("No valid GitHub repository URL found in issue")
    
    owner, repo_name = repo_match.groups()
    repo_name = repo_name.rstrip('.')  # Remove trailing period if any
    repo_url = f"https://github.com/{owner}/{repo_name}"
    
    # Extract PyPI package name (optional)
    pypi_match = re.search(r'PyPI Package Name.*?\n.*?([a-z0-9][a-z0-9-]*[a-z0-9])', body, re.IGNORECASE | re.DOTALL)
    pypi_name = pypi_match.group(1).strip() if pypi_match else None
    
    return {
        'owner': owner,
        'repo_name': repo_name,
        'repo_url': repo_url,
        'pypi_name': pypi_name
    }


def fetch_file_from_github(owner: str, repo_name: str, file_path: str, branch: str = 'main') -> Optional[str]:
    """Fetch a file from GitHub repository."""
    url = f"https://raw.githubusercontent.com/{owner}/{repo_name}/{branch}/{file_path}"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return response.text
        elif response.status_code == 404 and branch == 'main':
            # Try master branch
            return fetch_file_from_github(owner, repo_name, file_path, 'master')
        return None
    except Exception as e:
        print(f"Error fetching {file_path}: {e}", file=sys.stderr)
        return None


def parse_toml_simple(content: str) -> Dict:
    """Simple TOML parser for pyproject.toml."""
    try:
        import toml
        return toml.loads(content)
    except ImportError:
        # Fallback: simple regex-based parsing
        project_section = re.search(r'\[project\](.*?)(?=\[|$)', content, re.DOTALL)
        if not project_section:
            return {}
        
        project_text = project_section.group(1)
        result = {'project': {}}
        
        # Extract name
        name_match = re.search(r'name\s*=\s*["\']([^"\']+)["\']', project_text)
        if name_match:
            result['project']['name'] = name_match.group(1)
        
        # Extract version
        version_match = re.search(r'version\s*=\s*["\']([^"\']+)["\']', project_text)
        if version_match:
            result['project']['version'] = version_match.group(1)
        
        # Extract description
        desc_match = re.search(r'description\s*=\s*["\']([^"\']+)["\']', project_text)
        if desc_match:
            result['project']['description'] = desc_match.group(1)
        
        # Extract license
        license_match = re.search(r'license\s*=\s*\{[^}]*text\s*=\s*["\']([^"\']+)["\']', project_text)
        if license_match:
            result['project']['license'] = {'text': license_match.group(1)}
        
        # Extract keywords
        keywords_match = re.search(r'keywords\s*=\s*\[(.*?)\]', project_text, re.DOTALL)
        if keywords_match:
            keywords_text = keywords_match.group(1)
            keywords = re.findall(r'["\']([^"\']+)["\']', keywords_text)
            result['project']['keywords'] = keywords
        
        # Extract scripts
        scripts_match = re.search(r'\[project\.scripts\](.*?)(?=\[|$)', content, re.DOTALL)
        if scripts_match:
            scripts_text = scripts_match.group(1)
            scripts = {}
            for line in scripts_text.strip().split('\n'):
                script_match = re.match(r'([a-z0-9_-]+)\s*=', line.strip())
                if script_match:
                    scripts[script_match.group(1)] = True
            if scripts:
                result['project']['scripts'] = scripts
        
        return result


def validate_speckit(parsed_info: Dict) -> Tuple[bool, Dict, str]:
    """Validate speckit and extract metadata."""
    errors = []
    warnings = []
    
    owner = parsed_info['owner']
    repo_name = parsed_info['repo_name']
    
    # Fetch pyproject.toml
    pyproject_content = fetch_file_from_github(owner, repo_name, 'pyproject.toml')
    if not pyproject_content:
        return False, {}, "❌ Could not fetch `pyproject.toml` from repository. Please ensure the file exists in the root directory."
    
    # Parse pyproject.toml
    try:
        pyproject = parse_toml_simple(pyproject_content)
    except Exception as e:
        return False, {}, f"❌ Failed to parse `pyproject.toml`: {str(e)}"
    
    project = pyproject.get('project', {})
    
    # Validate required fields
    if not project.get('name'):
        errors.append("Missing `name` in [project]")
    if not project.get('version'):
        errors.append("Missing `version` in [project]")
    if not project.get('description'):
        errors.append("Missing `description` in [project]")
    
    # Check CLI commands
    scripts = project.get('scripts', {})
    if not scripts:
        warnings.append("No CLI commands found in [project.scripts] - this is unusual for a speckit")
    
    # Check README
    readme_content = fetch_file_from_github(owner, repo_name, 'README.md')
    if not readme_content:
        warnings.append("No README.md found - documentation is recommended")
    
    # If there are errors, return failure
    if errors:
        error_msg = "❌ **Validation errors:**\n\n" + "\n".join(f"- {e}" for e in errors)
        if warnings:
            error_msg += "\n\n⚠️ **Warnings:**\n\n" + "\n".join(f"- {w}" for w in warnings)
        return False, {}, error_msg
    
    # Build metadata
    metadata = {
        'name': project['name'],
        'version': project['version'],
        'description': project['description'],
        'repository': parsed_info['repo_url'],
        'pypi_package': parsed_info['pypi_name'] or project['name'],
        'cli_command': list(scripts.keys())[0] if scripts else project['name'],
        'license': project.get('license', {}).get('text', 'Unknown'),
        'tags': ','.join(project.get('keywords', [])),
        'created_at': '2025-11-09',
        'updated_at': '2025-11-09'
    }
    
    # Build summary
    summary = f"""✅ **Name**: `{metadata['name']}`
✅ **Version**: `{metadata['version']}`
✅ **CLI**: `{metadata['cli_command']}`
✅ **License**: {metadata['license']}"""
    
    if warnings:
        summary += "\n\n⚠️ **Warnings:**\n\n" + "\n".join(f"- {w}" for w in warnings)
    
    return True, metadata, summary


def main():
    """Main entry point."""
    issue_body = os.environ.get('ISSUE_BODY', '')
    if not issue_body:
        print("❌ ISSUE_BODY environment variable is required", file=sys.stderr)
        sys.exit(1)
    
    try:
        # Parse issue body
        parsed_info = parse_issue_body(issue_body)
        
        # Validate speckit
        valid, metadata, summary = validate_speckit(parsed_info)
        
        # Output to GitHub Actions
        github_output = os.environ.get('GITHUB_OUTPUT', '')
        if github_output:
            with open(github_output, 'a') as f:
                f.write(f"valid={str(valid).lower()}\n")
                if valid:
                    for key, value in metadata.items():
                        # Escape special characters for GitHub Actions
                        safe_value = str(value).replace('\n', '%0A').replace('\r', '%0D')
                        f.write(f"{key}={safe_value}\n")
                    f.write(f"summary<<EOF\n{summary}\nEOF\n")
                else:
                    f.write(f"error<<EOF\n{summary}\nEOF\n")
        
        # Print summary
        print(summary)
        
        sys.exit(0 if valid else 1)
    
    except Exception as e:
        error_msg = f"❌ **Unexpected error**: {str(e)}"
        print(error_msg, file=sys.stderr)
        
        github_output = os.environ.get('GITHUB_OUTPUT', '')
        if github_output:
            with open(github_output, 'a') as f:
                f.write(f"valid=false\n")
                f.write(f"error<<EOF\n{error_msg}\nEOF\n")
        
        sys.exit(1)


if __name__ == '__main__':
    main()

