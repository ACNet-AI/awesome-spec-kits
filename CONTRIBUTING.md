# Contributing to Awesome Spec Kits

Thank you for contributing! This guide will help you add your speckit to the awesome list.

## Quick Start

```bash
# 1. Create and publish your speckit
metaspec init my-awesome-speckit
cd my-awesome-speckit
# ... develop your speckit ...
uv build && uv publish

# 2. Generate metadata
metaspec register my-awesome-speckit --publish

# 3. Fork this repository
# https://github.com/ACNet-AI/awesome-spec-kits

# 4. Add your speckit
cp my-awesome-speckit-community.json speckits/
# Edit speckits.json to add your entry

# 5. Create Pull Request
```

## Submission Checklist

Before submitting, ensure:

- [ ] Speckit is published to PyPI
- [ ] `pip install <your-speckit>` works
- [ ] CLI command `<your-speckit> --help` works
- [ ] JSON file is valid (use `python scripts/validate.py`)
- [ ] Added to `speckits.json`
- [ ] README.md in your speckit repository
- [ ] Clear description and relevant tags

## Metadata Format

Your `<speckit-name>.json` must include:

```json
{
  "name": "Display Name",
  "command": "cli-command",
  "description": "Brief description (50-200 chars)",
  "pypi_package": "pypi-package-name",
  "repository": "https://github.com/...",
  "author": "Your Name",
  "version": "1.0.0",
  "tags": ["tag1", "tag2"],
  "cli_commands": ["cmd1", "cmd2"],
  "slash_commands": [],
  "source": "community",
  "is_builtin": false
}
```

### Field Requirements

- **name**: Human-readable, title case
- **command**: Lowercase, hyphens ok, must match CLI
- **description**: Clear, searchable, 50-200 characters
- **pypi_package**: Exact PyPI package name
- **repository**: Public GitHub/GitLab repository
- **tags**: 2-5 relevant tags, lowercase
- **cli_commands**: List of subcommands

## Tag Guidelines

Use standard, searchable tags:

**Domain**
- api, database, config, documentation, testing

**Protocol**
- openapi, graphql, grpc, rest, json-schema

**Function**
- validation, generation, linting, conversion

**Technology**
- yaml, json, xml, protobuf

## Review Process

1. **Automated checks**: JSON validation, PyPI verification
2. **Manual review**: Quality, security, relevance
3. **Feedback**: We may request changes
4. **Merge**: Usually within 1-3 days

## Updating Your Speckit

To update metadata:

1. Update your JSON file
2. Submit PR with changes
3. Increment version number

## Removing Your Speckit

To remove from list:

1. Submit PR removing your files
2. Explain reason (deprecated, renamed, etc.)

## Questions?

- Open an issue for questions
- See [MetaSpec documentation](https://github.com/zhaoyao8727/MetaSpec)

## Code of Conduct

Be respectful, constructive, and collaborative.

