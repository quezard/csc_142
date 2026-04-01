import pygame
import pygwidgets

pygame.init()

# Window setup
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 300
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Temperature Converter")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Clock
clock = pygame.time.Clock()

# --- Widgets ---

# Input box
inputField = pygwidgets.InputText(window, (50, 50), width=200)

# Radio buttons
radioFtoC = pygwidgets.TextRadioButton(window, (50, 100),
                                       "Fahrenheit to Celsius", group=1, value=True)

radioCtoF = pygwidgets.TextRadioButton(window, (50, 130),
                                       "Celsius to Fahrenheit", group=1)

# Button
convertButton = pygwidgets.TextButton(window, (50, 180), "Convert")

# Output display
outputText = pygwidgets.DisplayText(window, (50, 230), "")

# --- Main Loop ---
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Handle input box (ENTER key)
        if inputField.handleEvent(event):
            userText = inputField.getValue()
            try:
                temp = float(userText)

                if radioFtoC.getValue():
                    result = (temp - 32) / (9/5)
                    outputText.setValue(f"{result:.2f} °C")
                else:
                    result = temp * 9/5 + 32
                    outputText.setValue(f"{result:.2f} °F")

            except:
                outputText.setValue("Invalid input")

        # Handle radio buttons
        radioFtoC.handleEvent(event)
        radioCtoF.handleEvent(event)

        # Handle button click
        if convertButton.handleEvent(event):
            userText = inputField.getValue()
            try:
                temp = float(userText)

                if radioFtoC.getValue():
                    result = (temp - 32) / (9/5)
                    outputText.setValue(f"{result:.2f} °C")
                else:
                    result = temp * 9/5 + 32
                    outputText.setValue(f"{result:.2f} °F")

            except:
                outputText.setValue("Invalid input")

    # --- Draw ---
    window.fill(WHITE)

    inputField.draw()
    radioFtoC.draw()
    radioCtoF.draw()
    convertButton.draw()
    outputText.draw()

    pygame.display.update()
    clock.tick(30)

pygame.quit()