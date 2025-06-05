.. _contributing:

Contributing
============

We welcome contributions to ``intake-gfs-ncar``! This guide will help you get started with contributing to the project.

Code of Conduct
--------------

This project adheres to the Contributor Covenant `Code of Conduct <https://www.contributor-covenant.org/version/2/1/code_of_conduct/>`_. By participating, you are expected to uphold this code.

How to Contribute
----------------

1. **Report Bugs**
   - Check if the bug has already been reported in the `GitHub Issues <https://github.com/oceanum/intake-gfs-ncar/issues>`_
   - If not, open a new issue with a clear title and description
   - Include a minimal reproducible example if possible

2. **Suggest Enhancements**
   - Open an issue to discuss your proposed enhancement
   - Explain why this enhancement would be useful
   - Include any relevant examples or use cases

3. **Contribute Code**
   - Fork the repository and create a feature branch
   - Write tests for your changes
   - Ensure all tests pass
   - Submit a pull request with a clear description of your changes

Development Setup
---------------

1. **Fork and Clone**
   .. code-block:: bash

      git clone https://github.com/your-username/intake-gfs-ncar.git
      cd intake-gfs-ncar

2. **Create a Virtual Environment**
   .. code-block:: bash

      python -m venv venv
      source venv/bin/activate  # On Windows: venv\Scripts\activate

3. **Install Dependencies**
   .. code-block:: bash

      pip install -e ".[dev]"

4. **Run Tests**
   .. code-block:: bash

      pytest

Coding Standards
---------------

- Follow `PEP 8 <https://www.python.org/dev/peps/pep-0008/>`_ style guide
- Use type hints for all function signatures
- Write docstrings following the Google style guide
- Keep lines under 88 characters (Black will enforce this)
- Write tests for new functionality

Pull Request Process
-------------------

1. Update the README.md with details of changes if needed
2. Ensure tests pass and coverage is maintained
3. Update the CHANGELOG.md with your changes
4. The PR will be reviewed by maintainers

Documentation
------------

Documentation is built using Sphinx. To build it locally:

.. code-block:: bash

   cd docs
   make html

Open ``_build/html/index.html`` in your browser to view the documentation.

Release Process
--------------

1. Update the version number in ``__init__.py``
2. Update the CHANGELOG.md
3. Commit the changes with a message like "Bump version to X.Y.Z"
4. Create a git tag for the version: ``git tag vX.Y.Z``
5. Push the tag: ``git push origin vX.Y.Z``
6. The GitHub Actions workflow will automatically publish to PyPI

Questions?
----------

If you have any questions, feel free to open an issue on GitHub.
