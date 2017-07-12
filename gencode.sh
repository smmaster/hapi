mkdir -p build
rm -fr build/*
cd swagger
java -jar ~/swagger-codegen/modules/swagger-codegen-cli/target/swagger-codegen-cli.jar generate -l python-flask -i swagger.yaml -o ../build/ -c codegen.config

