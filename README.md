# Micropython Library

## Introduction

The **library** directory contains library files for various sensors that can be used with boards running Micropython firmware. You need to manually upload these library files to the board. Our customized firmware will automatically include these library files for ease of use.

The **main.py** under each directory in the **examples** directory are reference code samples for using the libraries under library. They can be directly uploaded to the board and run.

Below is a detailed list of libraries:

| module name | library | examples |
| ----------- | ------- | -------- |
| Servo | [library/servo.py](library/servo.py) | [examples/servo/set_angle/main.py](examples/servo/set_angle/main.py) |
| Passive buzzer | [library/buzzer.py](library/buzzer.py) | [examples/buzzer/play_a_melody/main.py](examples/buzzer/play_a_melody/main.py) |
| 8x8 Matrix LED | [library/matrix_led_8x8.py](library/matrix_led_8x8.py) | [examples/matrix_led_8x8/show/main.py](examples/matrix_led_8x8/show/main.py) |
| 4-digit 7-segment LED | [library/i2c_device.py](library/i2c_device.py)<br>[library/four_digit_led.py](library/four_digit_led.py)<br> | [examples/four_digit_led/show/main.py](examples/four_digit_led/show/main.py)|
| dht11 | This **dht** library is already built into the official firmware <br> refer to <https://docs.micropython.org/en/latest/esp32/quickref.html#dht-driver> | [examples/dht11/main.py](examples/dht11/main.py) |
| I2C LCD1602 | [library/lcd_i2c/lcd_i2c](library/lcd_i2c/lcd_i2c) <br> **Note: This library is a directory that contains multiple py files, so you need to upload the entire directory to board instead of uploading each file individually. For example, upload the library using the ampy command: `ampy -p COM1 put library/lcd_i2c/lcd_i2c`** <br> The library is from <https://github.com/brainelectronics/micropython-i2c-lcd> | [examples/i2c_lcd1602/main.py](examples/i2c_lcd1602/main.py) |

## Quick Start

First you need an ESP32 board running Micropython firmware. You can refer to the official documentation for downloading and flashing: <https://micropython.org/download/ESP32_GENERIC/>. It is recommended to download the latest v1.21.0 stable version directly: [**v1.21.0 (2023-10-05) .bin**](https://micropython.org/resources/firmware/ESP32_GENERIC-20231005-v1.21.0.bin)

After flashing, open any serial tool on your computer, select the USB port corresponding to your board, and set the baud rate to 115200. When you restart the board, you should see the serial tool printing Micropython version info normally, indicating successful flashing and running, like below:

```text
MicroPython v1.21.0-3 on 2023-11-22; Generic ESP32 module with ESP32
Type "help()" for more information.
>>>
```

## Update submodules

Update the submodules after you clone the repository. Update it with the following command:

```shell
git submodule update --init --recursive
```

## Upload Files

There are many command line and GUI tools for uploading files to Micropython. If you don't know which one to use, you can use the command line tool **adafruit-ampy**. Refer to the [official documentation](https://pypi.org/project/adafruit-ampy/) for installation and usage.

**ampy** uses serial port, so you need to stop the serial tool before using ampy. Then you can use the following commands to view the files on the ESP32 to verify if ampy is working properly. For example, if the ESP32 is connected to COM1 port on Windows, the command to list files is:

```shell
ampy -p COM1 ls
```

It should list **/boot.py** etc if working properly.

## Upload Libraries and Run Examples

Let's take a passive buzzer as an example. The corresponding library is **library/buzzer.py**. First upload the library file to the board:

```shell
ampy -p COM1 put library/buzzer.py
```

Then upload a buzzer example file as the main program, e.g. **examples/buzzer/play_a_melody/main.py**:

```shell
ampy -p COM1 put examples/buzzer/play_a_melody/main.py
```

After upload, restart the board and it will automatically run main.py, and you have successfully run an example program.

You can check the comments in each main.py under examples for documentation of the example programs.

If the library is a directory, you need to upload the entire directory to the board. Let's take a **I2C LCD1602** as an example:

```shell
ampy -p COM1 put library/lcd_i2c/lcd_i2c
```
