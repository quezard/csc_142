import pygame
import pygwidgets

pygame.init()

# Window
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 300
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Temperature Converter')

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Widgets
inputTemp = pygwidgets.InputText(window, (50, 50), 'Enter Temp:', width=200)

radioC = pygwidgets.TextRadioButton(window, (50, 100), 'Celsius', group=1, value=True)
radioF = pygwidgets.TextRadioButton(window, (200, 100), 'Fahrenheit', group=1)

convertButton = pygwidgets.TextButton(window, (50, 150), 'Convert')

outputText = pygwidgets.DisplayText(window, (50, 220), 'Result: ', fontSize=30)

clock = pygame.time.Clock()

# Main Loop
running = True
while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        inputTemp.handleEvent(event)

        # Button press
        if convertButton.handleEvent(event):

            try:
                temp = float(inputTemp.getValue())

                if radioC.getValue():  # Convert C → F
                    result = temp * 9/5 + 32
                    outputText.setValue(f"{result:.2f} °F")

                else:  # Convert F → C
                    result = (temp - 32) / (9/5)
                    outputText.setValue(f"{result:.2f} °C")

            except:
                outputText.setValue("Invalid Input")

        # Radio buttons
        radioC.handleEvent(event)
        radioF.handleEvent(event)

    # Draw screen
    window.fill(WHITE)

    inputTemp.draw()
    radioC.draw()
    radioF.draw()
    convertButton.draw()
    outputText.draw()

    pygame.display.update()
    clock.tick(30)

pygame.quit()