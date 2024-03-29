# Face-Recognition-System-with-GUI

<div align="justify">Face recognition system is a biometric system which automatically distinguish a particular person from a group and recognizes him the person. In this project, we are developing a facial recognition system with a GUI (graphical user interface) which uses a live feed (web cam) and recognizes the person real-time. The system consists of two major modes. One is the monitoring mode other is the detection mode. In monitoring mode, the system detects the faces. It has the ability to detect multiple people in the same frame. The detection mode recognizes the person and outputs his unique ID or the name. If that person is unknown, it simply displays ‘Unknown’. In addition, we can change the brightness of the frame and compare the modified frame with the original frame side to side. The images for the database and the information of the particular person is put into the database through a form which compromises of the fields username, name, age and address. When submitting the information, the system automatically takes series of photos of the person in front of the camera. These images are later used to train a model that can distinguish a particular person from the rest of the people in the database. This particular system can remove the records and the images of the people sequentially like a stack (Last In First Out).The database can be also reset by the user.</div>


<p align="center">
  <img src="https://github.com/tharakarehan/Face-Recognition-System-with-GUI/blob/master/Respo%20pics/Hnet-image-4.gif">
</p>

## Installation

Create a new conda environment. If you dont have conda installed download [miniconda](https://docs.conda.io/en/latest/miniconda.html)

```bash
conda create -n facereg python=3.6 
```
Clone this repository to your computer and navigate to the directory.

Activate new enviroment
```bash
conda activate facereg  
```
Install all the libraries used
```bash
pip install -r requirements.txt  
```

Then run the model

```bash
python modelFinal.py 
```

## Usage

### Monitoring Mode

<p align="center">
  <img wide=720 height=550 src="https://github.com/tharakarehan/Face-Recognition-System-with-GUI/blob/master/Respo%20pics/UI01.png">
</p>

#### ① - User Registration Button
<div align="justify">This gives you access to the database where all the information and the images of the people are displayed.</div>

#### ② - Monitor Button
<div align="justify">Monitor button will give access to the monitoring mode (from detection mode). Here only the faces are detected and a rectangle is drawn around the face. In addition, you can see the brightness adjustment panel on the right in this mode.</div>

#### ③ - Main Display Panel
<div align="justify">Main display panel displays the web cam feed continuously. In monitoring mode, the rectangle around the faces detected are shown through this panel. In detection mode, additionally names and the confidence levels are displayed. </div>

#### ④ - Detection Button
<div align="justify">Detection mode is activated. Recognized names will be displayed in the main panel and a image of the recognized person and his personal information are displayed at right side of the screen. </div>

#### ⑤ - Fill-out Form
<div align="justify">Information of the users are entered and stored to the database through this. </div>

#### ⑥ - Add Person Button
<div align="justify">This will submit the information and store them in the database. </div>

#### ⑦ - Secondary Display Panel
<div align="justify">TThis displays the web camera feed which is used to compare with the brightened or darkened frames. </div>

#### ⑧ - Secondary Display Panel (brightened)
<div align="justify">This displays the web camera feed after changing the brightness. </div>

#### ⑨ - Scaler for Brightness
<div align="justify">Scaler will adjust the brightness. By moving the slider to the right, brightness can be increased. By moving to left, brightness can be reduced. </div>

#### ⑩ - Quit Button
<div align="justify">This will close the application. </div>

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)