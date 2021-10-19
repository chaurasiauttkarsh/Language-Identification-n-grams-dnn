# Language-Identification-n-grams-dnn

Dense Neural Network is trained on character level n-grams to build langauge identification model.</br>

WiLI-2018, the Wikipedia language identification benchmark dataset, contains 235000 paragraphs of 235 languages. Each language in this dataset contains 1000 rows/paragraphs. The following is the subset of dataset used:

⦁ English ⦁ Arabic ⦁ French ⦁ Hindi ⦁ Urdu ⦁ Portuguese ⦁ Persian ⦁ Pushto ⦁ Spanish ⦁ Korean ⦁ Tamil ⦁ Turkish ⦁ Estonian ⦁ Russian ⦁ Romanian ⦁ Chinese ⦁ Swedish ⦁ Latin ⦁ Indonesian ⦁ Dutch ⦁ Japanese ⦁ Thai

1. Data: Contains dataset used for language identification</br>
-dataset.csv</br>
2. Model: Contains model and parameter files used for language identification</br>
-model.h5</br>
-parameters.sav</br>
3. PDF Google Colab Output: This contains the output obtained in a pdf format</br>
-Identification.pdf</br>
-Training Model.pdf</br>
4. ColabNotebook: Contains output of training and identification. Link to the colab files is also present</br>
-Language_Identification.ipynb</br>
-Language_Identification_Prediction.ipynb</br>
5. predict-local.py: this file is used to make predictions in local system(environment should be created and dependencies needs to be installed before running this file)</br>
Required Dependencies:
- tensorflow r2.6
- pickle
- numpy
- re
- pandas</br>
(It is recommended to run ColabNotebook/Language_Identification_Prediction.ipynb file on google colab where latest dependencies are taken care of)</br>

Please use larger copus for language identification purpose in the case of syntactically similar languages.



