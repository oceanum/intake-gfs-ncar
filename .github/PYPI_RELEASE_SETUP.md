# PyPI Release Setup for intake-gfs-ncar

This document describes the automated PyPI release setup implemented for the `intake-gfs-ncar` project.

## Overview

The project now includes a comprehensive GitHub Actions workflow system for automated building, testing, and releasing to PyPI. This eliminates the need for manual package uploads and ensures consistent, reliable releases.

## Workflow Files

### 1. `.github/workflows/release.yml`
**Purpose**: Main release workflow that publishes to PyPI
**Triggers**: 
- Git tags matching `v*` pattern (e.g., `v0.3.0`, `v1.0.0`)
- Manual workflow dispatch with optional Test PyPI publishing

**Features**:
- Builds both source distribution (sdist) and wheel
- Runs comprehensive tests across Python 3.9, 3.10, and 3.11
- Uses PyPI trusted publishing (no API tokens required)
- Creates GitHub releases with built artifacts
- Extracts release notes from `CHANGELOG.md`
- Supports both production PyPI and Test PyPI

### 2. `.github/workflows/build-test.yml`
**Purpose**: Tests package building on pull requests
**Triggers**: Pull requests and pushes to main branch

**Features**:
- Validates package can be built successfully
- Tests installation from both wheel and source distributions
- Validates package metadata
- Checks README rendering
- Runs on every PR to catch build issues early

### 3. `.github/workflows/python-tests.yml` (Enhanced)
**Purpose**: Comprehensive testing and code quality checks
**Triggers**: Pull requests and pushes to main branch

**Features**:
- Tests across Python 3.9, 3.10, and 3.11
- Code formatting checks (Black, isort)
- Linting (flake8)
- Type checking (mypy)
- Coverage reporting with Codecov integration

## Release Process

### Automated Release (Recommended)

1. **Prepare the release** using the helper script:
   ```bash
   # Test what would happen
   python scripts/release.py --version 0.3.0 --dry-run
   
   # Prepare the actual release
   python scripts/release.py --version 0.3.0
   ```

2. **Push to trigger the release**:
   ```bash
   git push origin main
   git push origin v0.3.0
   ```

3. **Monitor the release** at [GitHub Actions](https://github.com/oceanum/intake-gfs-ncar/actions)

The workflow will automatically:
- ✅ Run all tests
- ✅ Build source and wheel distributions
- ✅ Publish to PyPI
- ✅ Create GitHub release with artifacts
- ✅ Extract release notes from changelog

### Manual Testing

To test releases before production:

```bash
# Trigger test release to Test PyPI
gh workflow run release.yml --field test_release=true
```

## GitHub Repository Configuration

### Required Environments

The repository must have these environments configured:

1. **`pypi`** - For production PyPI releases
   - Protection rules: Require reviewers for production releases
   - PyPI trusted publishing configured

2. **`test-pypi`** - For test releases
   - PyPI trusted publishing configured for Test PyPI

### PyPI Trusted Publishing Setup

Both PyPI and Test PyPI are configured to trust this GitHub repository:

- **Repository**: `oceanum/intake-gfs-ncar`
- **Workflow**: `release.yml`
- **Environment**: `pypi` (for PyPI) / `test-pypi` (for Test PyPI)

This eliminates the need for API tokens and provides better security.

## Release Helper Script

### Location
`scripts/release.py`

### Features
- ✅ Version format validation (semantic versioning)
- ✅ Git status checking (clean working directory)
- ✅ Automatic version updating in `pyproject.toml`
- ✅ Git tag creation
- ✅ Dry-run support for testing
- ✅ Comprehensive error checking

### Usage Examples

```bash
# Check what would happen
python scripts/release.py --version 0.3.0 --dry-run

# Prepare release
python scripts/release.py --version 0.3.0

# Prepare pre-release
python scripts/release.py --version 0.3.0-rc.1
```

## Package Build Configuration

### Key Files Updated
- `pyproject.toml` - Modern SPDX license format, proper metadata
- `MANIFEST.in` - Includes all necessary files in distribution
- `requirements-dev.txt` - Added build and validation tools

### Build Tools
- `build` - PEP 517 compliant building
- `twine` - Distribution validation and uploading
- `check-manifest` - Manifest validation
- `readme-renderer` - README validation

## Testing

### Release Script Tests
- Located in `tests/test_release_script.py`
- Covers all core functionality
- Integration tests for main workflow
- Edge case validation

### Package Build Tests
- Automated in GitHub Actions
- Tests installation from both wheel and source
- Validates metadata and README rendering

## Security Features

1. **Trusted Publishing** - No API tokens stored in repository
2. **Environment Protection** - Production releases require approval
3. **Comprehensive Testing** - All code tested before release
4. **Clean Git History** - Requires clean working directory

## Monitoring and Troubleshooting

### GitHub Actions Dashboard
- Monitor all workflows: https://github.com/oceanum/intake-gfs-ncar/actions
- Check workflow runs, logs, and artifacts

### Common Issues
1. **Failed Tests** - Check test logs, fix issues before releasing
2. **Build Failures** - Verify package metadata and dependencies
3. **PyPI Upload Failures** - Check trusted publishing configuration

### Debug Commands
```bash
# Test local build
python -m build
python -m twine check dist/*

# Test installation
pip install dist/*.whl
python -c "import intake_gfs_ncar; print('Success!')"
```

## Future Enhancements

Potential improvements for the release system:

- [ ] Automatic changelog generation from git commits
- [ ] Automated dependency updates using Dependabot
- [ ] Performance benchmarking in CI
- [ ] Automated documentation deployment
- [ ] Release candidate automation
- [ ] Slack/email notifications for releases

## Documentation Links

- [PyPI Trusted Publishing](https://docs.pypi.org/trusted-publishers/)
- [GitHub Actions Workflows](https://docs.github.com/en/actions/using-workflows)
- [Python Packaging](https://packaging.python.org/)
- [Semantic Versioning](https://semver.org/)