FROM maven:3.9.4-eclipse-temurin-11

# Create app directory
WORKDIR /usr/src/app

# Copy pom and sources
COPY pom.xml .
COPY src ./src

# Run tests (will download dependencies)
RUN mvn -B test

CMD ["/bin/bash"]
