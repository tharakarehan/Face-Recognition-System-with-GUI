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

### -Monitoring Mode

<p align="center">
  <img wide=720 height=550 src="https://github.com/tharakarehan/Face-Recognition-System-with-GUI/blob/master/Respo%20pics/UI01.png">
</p>



## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)