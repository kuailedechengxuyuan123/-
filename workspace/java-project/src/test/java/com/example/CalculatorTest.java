package com.example;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Nested;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;

public class CalculatorTest {

    private final Calculator calc = new Calculator();

    @Nested
    @DisplayName("Addition tests")
    class AddTests {
        @Test
        void addPositiveNumbers() {
            assertEquals(5, calc.add(2, 3));
        }

        @ParameterizedTest(name = "add({0}, {1}) = {2}")
        @CsvSource({
            "0, 0, 0",
            "1, -1, 0",
            "-2, -3, -5",
            "100, 200, 300"
        })
        void paramAdd(int a, int b, int expected) {
            assertEquals(expected, calc.add(a, b));
        }
    }

    @Test
    @DisplayName("Subtraction should work")
    void subtractTest() {
        assertEquals(1, calc.subtract(3, 2));
        assertEquals(-5, calc.subtract(-3, 2));
    }

    @Test
    @DisplayName("Multiplication should work")
    void multiplyTest() {
        assertEquals(6, calc.multiply(2, 3));
        assertEquals(0, calc.multiply(0, 5));
    }

    @Nested
    @DisplayName("Division tests")
    class DivisionTests {
        @Test
        void divideNormal() {
            assertEquals(2.0, calc.divide(6.0, 3.0), 1e-9);
        }

        @Test
        void divideFractional() {
            assertEquals(0.5, calc.divide(1.0, 2.0), 1e-9);
        }

        @Test
        @DisplayName("Divide by zero should throw")
        void divideByZero() {
            Exception ex = assertThrows(IllegalArgumentException.class, () -> calc.divide(1.0, 0.0));
            assertTrue(ex.getMessage().contains("Cannot divide by zero"));
        }
    }
}
