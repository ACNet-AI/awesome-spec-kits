# Awesome Spec Kits [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of awesome specification toolkits (speckits) for spec-driven development

Specification toolkits that drive AI to generate content. Define specs, let AI create code, docs, configs, tests, protocols, and more. Spec-Driven X (SD-X) for the AI era.

## Contents

- [What is a Speckit?](#what-is-a-speckit)
- [Available Speckits](#available-speckits)
- [Using Speckits](#using-speckits)
- [Contributing](#contributing)
- [Resources](#resources)

## What is a Speckit?

A **speckit** (specification toolkit) drives AI to generate content from specifications:

- 📝 **Define** specifications for your domain (API, protocols, configs, etc.)
- 🤖 **AI Generates** - Specs drive AI to create code, docs, configs, tests, designs, protocols
- ✅ **Validate** - Specs validate AI-generated content for quality and conformance
- 🎯 **Consistency** - Same spec ensures consistent outputs across the board
- 🚀 **Automation** - Specs automate what would be manual work

**Spec-Driven X (SD-X)** philosophy: **Specs → AI → X (Anything)**

Whether you're building:
- **SD-Development** - Specs → AI → Code, tests, implementations
- **SD-Design** - Specs → AI → UI designs, architectures
- **SD-Protocol** - Specs → AI → Protocol definitions, standards
- **SD-Documentation** - Specs → AI → Docs, guides, tutorials
- **SD-API** - API specs → AI → Client SDKs, server implementations
- **SD-Config** - Config specs → AI → System configurations
- **SD-Test** - Test specs → AI → Test cases, scenarios
- **SD-X** - Any domain where specs drive AI generation

Speckits make specifications the **single source of truth** that drives AI.

**How to build a speckit?** Any way you want! Build from scratch, use a framework, or adapt existing tools - as long as it follows spec-driven principles. [MetaSpec](https://github.com/ACNet-AI/MetaSpec) is one option if you want a framework, but you're completely free to implement your own solution in any language with any approach.

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

- [GitHub Spec-Kit](https://github.com/github/spec-kit) - Official Spec-Driven Development toolkit (46.6k+ stars)
- [MetaSpec Framework](https://github.com/ACNet-AI/MetaSpec) - Meta-specification framework for creating speckits
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

