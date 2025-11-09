#!/usr/bin/env python3
"""
Add speckit to registry JSON file.
"""
import json
import argparse
from datetime import datetime


def add_to_registry(metadata: dict, registry_file: str):
    """Add or update speckit in registry."""
    # Read existing registry
    try:
        with open(registry_file, 'r', encoding='utf-8') as f:
            registry = json.load(f)
    except FileNotFoundError:
        registry = {
            'version': '1.0',
            'last_updated': datetime.utcnow().isoformat() + 'Z',
            'speckits': []
        }
    
    # Ensure speckits key exists
    if 'speckits' not in registry:
        registry['speckits'] = []
    
    # Check if speckit already exists
    existing_index = None
    for i, speckit in enumerate(registry['speckits']):
        if speckit.get('name') == metadata['name']:
            existing_index = i
            break
    
    # Build speckit entry
    speckit_entry = {
        'name': metadata['name'],
        'version': metadata['version'],
        'description': metadata['description'],
        'repository': metadata['repository'],
        'pypi_package': metadata['pypi_package'],
        'cli_command': metadata['cli_command'],
        'license': metadata['license'],
        'tags': metadata['tags'].split(',') if metadata['tags'] else [],
        'created_at': metadata.get('created_at', datetime.utcnow().strftime('%Y-%m-%d')),
        'updated_at': datetime.utcnow().strftime('%Y-%m-%d'),
        'status': 'active'
    }
    
    # Add or update
    if existing_index is not None:
        # Update existing entry (preserve created_at)
        speckit_entry['created_at'] = registry['speckits'][existing_index].get('created_at', speckit_entry['created_at'])
        registry['speckits'][existing_index] = speckit_entry
        print(f"✅ Updated {metadata['name']} in registry")
    else:
        # Add new entry
        registry['speckits'].append(speckit_entry)
        print(f"✅ Added {metadata['name']} to registry")
    
    # Sort by name
    registry['speckits'].sort(key=lambda x: x['name'])
    
    # Update last_updated
    registry['last_updated'] = datetime.utcnow().isoformat() + 'Z'
    
    # Write back to file
    with open(registry_file, 'w', encoding='utf-8') as f:
        json.dump(registry, f, indent=2, ensure_ascii=False)
        f.write('\n')  # Add trailing newline
    
    print(f"📝 Registry updated: {registry_file}")
    print(f"📊 Total speckits: {len(registry['speckits'])}")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description='Add speckit to registry')
    parser.add_argument('--name', required=True, help='Speckit name')
    parser.add_argument('--version', required=True, help='Speckit version')
    parser.add_argument('--description', required=True, help='Speckit description')
    parser.add_argument('--repository', required=True, help='GitHub repository URL')
    parser.add_argument('--pypi', required=True, help='PyPI package name')
    parser.add_argument('--cli', required=True, help='CLI command name')
    parser.add_argument('--license', required=True, help='License type')
    parser.add_argument('--tags', default='', help='Comma-separated tags')
    parser.add_argument('--registry', default='speckits.json', help='Registry file path')
    
    args = parser.parse_args()
    
    metadata = {
        'name': args.name,
        'version': args.version,
        'description': args.description,
        'repository': args.repository,
        'pypi_package': args.pypi,
        'cli_command': args.cli,
        'license': args.license,
        'tags': args.tags
    }
    
    add_to_registry(metadata, args.registry)


if __name__ == '__main__':
    main()

