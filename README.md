# Awesome Spec Kits [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of awesome specification toolkits (speckits) for spec-driven development

Specification toolkits that use specifications to drive content generation. Define specs once, generate anything - code, docs, configs, tests, and more. Spec-Driven X (SD-X) for the AI era.

## Contents

- [What is a Speckit?](#what-is-a-speckit)
- [Available Speckits](#available-speckits)
- [Using Speckits](#using-speckits)
- [Contributing](#contributing)
- [Resources](#resources)

## What is a Speckit?

A **speckit** (specification toolkit) uses specifications to **drive content generation**:

- 📝 **Define** clear specifications for your domain (API, protocols, configs, etc.)
- 🤖 **Generate** content from specifications (code, docs, configs, tests, schemas, etc.)
- ✅ **Validate** generated content against specifications
- 🎯 **Ensure** consistency and quality across outputs
- 🚀 **Automate** content creation with spec-driven workflows

Speckits embody the **Spec-Driven X (SD-X)** philosophy: define once, generate many. Whether you're creating API toolkits (SD-API), configuration tools (SD-Config), or documentation generators (SD-Docs), speckits make specifications the single source of truth.

Speckits can be built with any framework or tool. [MetaSpec](https://github.com/ACNet-AI/MetaSpec) is one popular framework for creating speckits, but you're welcome to use any technology stack that follows spec-driven development principles.

## Available Speckits

*No speckits submitted yet - be the first to contribute!*

<!--
### API & REST

- [api-spec-kit](https://github.com/example/api-spec-kit) - REST API specification toolkit

### Protocols

- [mcp-spec-kit](https://github.com/example/mcp-spec-kit) - Model Context Protocol toolkit

### Configuration

- [config-spec-kit](https://github.com/example/config-spec-kit) - Configuration validation
-->

## Using Speckits

### Search and Install

```bash
# Install MetaSpec
pip install meta-spec

# Search for speckits
metaspec search "api validation"

# List all available
metaspec list

# Install a speckit
metaspec install <speckit-name>
```

### Direct Installation

```bash
# Install from PyPI
pip install <speckit-name>

# Use directly
<speckit-name> --help
```

## Contributing

Have a speckit to share? **We'd love to have it!**

### 🚀 Automated Registration (Recommended)

**1-Click Registration via Issue Template:**

1. Go to [**Create Registration Issue**](../../issues/new?template=register-speckit.yml)
2. Fill in your speckit's GitHub repository URL
3. Submit the issue
4. **Done!** Our bot will:
   - ✅ Validate your speckit
   - ✅ Extract metadata from `pyproject.toml`
   - ✅ Create a PR automatically
   - ✅ Notify you of the result

**Requirements**:
- Valid `pyproject.toml` with name, version, description
- `README.md` with documentation
- Working CLI commands in `[project.scripts]`
- Open source license

### Manual Submission (Alternative)

If you prefer the traditional way:

```bash
# 1. Fork this repo
# 2. Edit speckits.json
# 3. Add your speckit entry
# 4. Create PR
```

See [CONTRIBUTING.md](./CONTRIBUTING.md) for detailed guidelines.

### Quality Standards

We maintain quality to ensure good user experience:
- Clear, searchable descriptions
- Relevant tags
- Active maintenance
- Follows naming conventions

## Resources

- [MetaSpec Framework](https://github.com/ACNet-AI/MetaSpec) - A popular framework for creating speckits
- [MetaSpec Documentation](https://github.com/ACNet-AI/MetaSpec/tree/main/docs)
- [Creating a Speckit with MetaSpec](https://github.com/ACNet-AI/MetaSpec/blob/main/docs/quickstart.md)

## Statistics

- **Total Speckits**: 0
- **Contributors**: 0
- **Last Updated**: 2025-11-09

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

This list is released under CC0 (Public Domain). Individual speckits have their own licenses.

## Acknowledgments

Maintained by the [ACNet-AI](https://github.com/ACNet-AI) community and [MetaSpec](https://github.com/ACNet-AI/MetaSpec) contributors.

