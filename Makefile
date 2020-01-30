all: test

test: 
	@cd solutions; \
        for file in *.py; do \
            python $$file; \
        done

