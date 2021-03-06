#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise

    try:
        import settings as settings_mod  # Assumed to be in the same directory.
    except ImportError:
        sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r" % __file__)
        sys.exit(1)

    sys.path.insert(0, settings_mod.BASE_DIR)

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "testproject.settings")
    execute_from_command_line(sys.argv)
