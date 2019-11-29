#Inspiration
People with hearing impairment are safe and capable drivers, although there remains some environmental cues which they cannot detect while on the road. We developed a tool that creates a safer driving experience by alerting hearing impaired drivers of other incoming vehicles.

#What it does
Three microphones are set up around a vehicle so that it samples sound from the environment in 360 degrees. If our machine-learning SVM algorithm detects an ambulance or honking car in the nearby area, it localizes the object based on the difference in amplitude of sound detected by each microphone and the time of delay between each microphone.

#How we built
We connected three microphones to an Arduino Uno for sound detection. The amplitude of sound and the time of sound detection was read from the Arduino and channeled into a raspberry-pi for further processing. In Python, we used supervised learning with a support vector machine to detect whether a nearby sound was the siren of an ambulance or the persistent honk of a nearby car. Taking into account which microphone was persistently detecting the loudest sound, and the position of the microphone in relation to the driver, a dynamic GUI displays an arrow that tracks the position of the incoming vehicle to alert the driver.

#Difficulties encountered
Adjusting the sensitivity of the microphones so that they were providing rich enough data for training our machine learning algorithm. Interfacing the Arduino Uno with the Raspberry-Pi. Controlling our data flow so that our tool could support alerting from real-time data.

#What we're proud of
Setting up the hardware so that we could sensitively detect sounds in the environment, feeding that data into a raspberry-pi, and performing processing and supervised machine-learning in real-time.

#What we learned
We all started the project with zero experience in using Raspberry Pis or Arduinos so there was quite a learning curve for all of us. We also had never worked with triangulation, python GUIs or classifying sound data. We learned quite a bit about each topic through the course of the weekend.

#Next steps
Integrating more microphones for more sensitive and accurate 360 degree sound detection. Implementing microphones into vehicles in an effective but non-intrusive way. Training our algorithm on more environmental threats so that we may alert drivers.
