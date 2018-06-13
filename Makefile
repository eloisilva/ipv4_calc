clean:
	@echo "Cleaning control files"
	@if test -d ipv4_calc.egg-info ;then rm -r ipv4_calc.egg-info/ ;fi
	@if test -d build ;then rm -r build/ ;fi
	@if test -d dist ;then rm -r dist/ ;fi

clean-py:
	@echo "Cleaning python artifacts"
	@find . -type f -name '*.pyc' -delete
	@find . -type d -name '__pycache__' -delete

clean-all: clean-py clean

test:
	@/usr/bin/python3 ipv4_calc

all: clean-all test
