# Setup
1. install plugins: $ pip install -r requirements.txt
2. check installed-plugins: $ pip freeze

# Execute
- with mark: $ pytest -m smoke
- with xdist: $ pytest -n=3
- with option: $ pytest --browser=firefox