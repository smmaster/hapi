mkdir -p build
rm -fr build/*
java -jar ~/swagger-codegen/modules/swagger-codegen-cli/target/swagger-codegen-cli.jar generate -l python-flask -i jobManager.yaml -o build/job -c codegen.config

