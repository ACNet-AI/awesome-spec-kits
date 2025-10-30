# Awesome Spec Kits [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of awesome specification toolkits (speckits) built with [MetaSpec](https://github.com/zhaoyao8727/MetaSpec)

Specification toolkits that help you define, validate, and enforce specifications in your projects.

## Contents

- [What is a Speckit?](#what-is-a-speckit)
- [Available Speckits](#available-speckits)
- [Using Speckits](#using-speckits)
- [Contributing](#contributing)
- [Resources](#resources)

## What is a Speckit?

A **speckit** (specification toolkit) is a command-line tool that helps you:
- ✅ Define specifications for your domain (API, config, protocols, etc.)
- 🔍 Validate files against specifications
- 🚀 Generate boilerplate from specifications
- 📚 Maintain consistency across projects

Built with [MetaSpec](https://github.com/zhaoyao8727/MetaSpec), speckits follow spec-driven development principles.

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
metaspec register --search "api validation"

# List all available
metaspec register --list-community

# Install a speckit
metaspec register --install <speckit-name>
```

### Direct Installation

```bash
# Install from PyPI
pip install <speckit-name>

# Use directly
<speckit-name> --help

# Or via MetaSpec
metaspec spec <speckit-name> <command>
```

## Contributing

Have a speckit to share? **We'd love to have it!**

### Quick Submit

```bash
# 1. Create your speckit
metaspec init my-awesome-speckit

# 2. Publish to PyPI
uv build && uv publish

# 3. Generate metadata
metaspec register my-awesome-speckit --publish

# 4. Fork this repo and create PR
```

See [CONTRIBUTING.md](./CONTRIBUTING.md) for detailed guidelines.

### Submission Requirements

- ✅ Published to PyPI
- ✅ Working CLI commands
- ✅ Basic documentation (README)
- ✅ Valid metadata

### Quality Standards

We maintain quality to ensure good user experience:
- Clear, searchable descriptions
- Relevant tags
- Active maintenance
- Follows naming conventions

## Resources

- [MetaSpec Documentation](https://github.com/zhaoyao8727/MetaSpec/tree/main/docs)
- [Creating a Speckit](https://github.com/zhaoyao8727/MetaSpec/blob/main/docs/quickstart.md)
- [Community Guide](https://github.com/zhaoyao8727/MetaSpec/blob/main/docs/community-registry.md)

## Statistics

- **Total Speckits**: 0
- **Contributors**: 0
- **Last Updated**: 2024-01-15

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

This list is released under CC0 (Public Domain). Individual speckits have their own licenses.

## Acknowledgments

Maintained by the [ACNet-AI](https://github.com/ACNet-AI) community and [MetaSpec](https://github.com/zhaoyao8727/MetaSpec) contributors.

