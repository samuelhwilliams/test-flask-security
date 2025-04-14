Run `uv run hello.py`

It errors.

```
test-flask-security on  main is 📦 v0.1.0 via 🐍 v3.13.2
✦2 ❯ uv run hello.py
Traceback (most recent call last):
  File "/Users/sam/git/test-flask-security/hello.py", line 1, in <module>
    from flask_security.utils import validate_redirect_url
  File "/Users/sam/git/test-flask-security/.venv/lib/python3.13/site-packages/flask_security/__init__.py", line 17, in <module>
    from .core import (
    ...<6 lines>...
    )
  File "/Users/sam/git/test-flask-security/.venv/lib/python3.13/site-packages/flask_security/core.py", line 92, in <module>
    from .totp import Totp
  File "/Users/sam/git/test-flask-security/.venv/lib/python3.13/site-packages/flask_security/totp.py", line 18, in <module>
    from passlib.pwd import genword
  File "/Users/sam/git/test-flask-security/.venv/lib/python3.13/site-packages/passlib/pwd.py", line 16, in <module>
    import pkg_resources
ModuleNotFoundError: No module named 'pkg_resources'

```
