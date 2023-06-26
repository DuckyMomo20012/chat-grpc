.PHONY: gen-proto
gen-proto:
	@echo "Generating proto files..."

	cd ./proto && buf generate

	@echo "Done"
