# Run Calculator JUnit tests with Docker

This project contains a simple Java Maven project (`Calculator`) and JUnit 5 tests.
If you don't have Maven or JDK installed locally, you can run the tests inside Docker.

Prerequisites
- Docker installed and running on your machine.

Build and run tests (PowerShell)

```powershell
# from repository root
cd C:\workspace\java-project

# Build the Docker image (tags as calculator-test)
docker build -t calculator-test .

# Run the container (the tests already ran during build). To inspect the container interactively:
docker run --rm -it calculator-test

# After build, Maven test output and surefire reports are available in the image build layers;
# to see reports locally, run tests without --rm and copy out the reports, or mount a volume:
docker run --rm -v ${PWD}:/usr/src/app -w /usr/src/app calculator-test mvn test

```

Expected results
- Maven will run the JUnit tests and print a summary similar to:

```
[INFO] -------------------------------------------------------
[INFO]  T E S T S
[INFO] -------------------------------------------------------
[INFO] Running com.example.CalculatorTest
[INFO] Tests run: 6, Failures: 0, Errors: 0, Skipped: 0, Time elapsed: 0.123 s - in com.example.CalculatorTest
[INFO]
[INFO] Results:
[INFO]
[INFO] Tests run: 6, Failures: 0, Errors: 0, Skipped: 0
[INFO]
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
```

Artifacts
- Surefire reports (XML/text) will be in `target/surefire-reports` inside the project folder when you run `mvn test` with a mounted volume.
