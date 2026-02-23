import pygame
import pygwidgets
import sys

pygame.init()

# Window setup
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 300
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Temperature Converter")

clock = pygame.time.Clock()

# Widgets
inputBox = pygwidgets.InputText(window, (50, 50), width=200)

# Radio buttons: group=1 passed positionally
radioFtoC = pygwidgets.TextRadioButton(window, (50, 100),
                                       "Fahrenheit to Celsius",
                                       1, True)

radioCtoF = pygwidgets.TextRadioButton(window, (50, 130),
                                       "Celsius to Fahrenheit",
                                       1)

convertButton = pygwidgets.TextButton(window, (50, 180), "Convert")

outputDisplay = pygwidgets.DisplayText(window, (50, 230),
                                       value="Result will appear here",
                                       fontSize=24)


def convertTemperature():
    """Convert the input temperature based on selected radio button"""
    text = inputBox.getValue()

    try:
        temp = float(text)

        if radioFtoC.getValue():
            # Fahrenheit to Celsius
            result = (temp - 32) / (9 / 5)
            outputDisplay.setValue(f"{result:.2f} °C")  # ✅ string with units
        else:
            # Celsius to Fahrenheit
            result = temp * 9 / 5 + 32
            outputDisplay.setValue(f"{result:.2f} °F")  # ✅ string with units

    except ValueError:
        outputDisplay.setValue("Invalid input")  # ✅ always string


# Main loop
while True:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Handle events for widgets
        inputBox.handleEvent(event)
        radioFtoC.handleEvent(event)
        radioCtoF.handleEvent(event)

        # A. Press Enter in TextInput
        if inputBox.handleEvent(event):
            convertTemperature()

        # B. Changing selected radio button
        if radioFtoC.handleEvent(event) or radioCtoF.handleEvent(event):
            convertTemperature()

        # C. Press Convert button
        if convertButton.handleEvent(event):
            convertTemperature()

    # Draw everything
    window.fill((240, 240, 240))

    inputBox.draw()
    radioFtoC.draw()
    radioCtoF.draw()
    convertButton.draw()
    outputDisplay.draw()

    pygame.display.update()