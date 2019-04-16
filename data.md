
__Example of the data:__

__Training File1:__ S0004-06142005000500011-1.txt

`Datos del paciente.
Nombre:  Ernesto.
Apellidos: Rivera Bueno.
NHC: 368503.
NASS: 26 63514095.
Domicilio:  Calle Miguel Benitez 90.
Localidad/ Provincia: Madrid.
CP: 28016.
Datos asistenciales.
Fecha de nacimiento: 03/03/1946.
País: España.
Edad: 70 años Sexo: H.
Fecha de Ingreso: 12/12/2016.
Médico:  Ignacio Navarro Cuéllar NºCol: 28 28 70973.
Informe clínico del paciente: Paciente de 70 años de edad, minero jubilado, sin alergias medicamentosas conocidas, que presenta como antecedentes personales: accidente laboral antiguo con fracturas vertebrales y costales; intervenido de enfermedad de Dupuytren en mano derecha y by-pass iliofemoral izquierdo; Diabetes Mellitus tipo II, hipercolesterolemia e hiperuricemia; enolismo activo, fumador de 20 cigarrillos / día.
Es derivado desde Atención Primaria por presentar hematuria macroscópica postmiccional en una ocasión y microhematuria persistente posteriormente, con micciones normales.
En la exploración física presenta un buen estado general, con abdomen y genitales normales; tacto rectal compatible con adenoma de próstata grado I/IV.
En la analítica de orina destaca la existencia de 4 hematíes/ campo y 0-5 leucocitos/campo; resto de sedimento normal.
Hemograma normal; en la bioquímica destaca una glucemia de 169 mg/dl y triglicéridos de 456 mg/dl; función hepática y renal normal. PSA de 1.16 ng/ml.
Las citologías de orina son repetidamente sospechosas de malignidad.
En la placa simple de abdomen se valoran cambios degenerativos en columna lumbar y calcificaciones vasculares en ambos hipocondrios y en pelvis.
La ecografía urológica pone de manifiesto la existencia de quistes corticales simples en riñón derecho, vejiga sin alteraciones con buena capacidad y próstata con un peso de 30 g.
En la UIV se observa normofuncionalismo renal bilateral, calcificaciones sobre silueta renal derecha y uréteres arrosariados con imágenes de adición en el tercio superior de ambos uréteres, en relación a pseudodiverticulosis ureteral. El cistograma demuestra una vejiga con buena capacidad, pero paredes trabeculadas en relación a vejiga de esfuerzo. La TC abdominal es normal.
La cistoscopia descubre la existencia de pequeñas tumoraciones vesicales, realizándose resección transuretral con el resultado anatomopatológico de carcinoma urotelial superficial de vejiga.
Remitido por: Ignacio Navarro Cuéllar c/ del Abedul 5-7, 2º dcha 28036 Madrid, España E-mail: nnavcu@hotmail.com.`

__Description:__

`The training file consists of plain text representing a clinical case study. It has Protected Health Information (PHI) 
which is any information in the medical record that can be used to identify an individual, and that was created, used, 
or disclosed in the course of providing a health care service, such as a diagnosis or treatment. In other words, PHI is 
personally identifiable information in medical records, including conversations between doctors and nurses about treatment. 
PHI also includes billing information and any patient-identifiable information in a health insurance company's computer system.`

Some information that can be considered PHI
❏ Names
❏ Surnames
❏ Addresses
❏ Hospitals
❏ Professions
❏ Different types of locations (provinces, cities, towns,…)
❏ Billing information
❏ Email
❏ Phone records`


__Training File1 Gold Annotations:__ S0004-06142005000500011-1.ann

The following text shows an example of an annotation in the BRAT format.

`T1	FECHAS 215 225	03/03/1946
T2	CORREO_ELECTRONICO 2421 2439	nnavcu@hotmail.com
T3	PAIS 2406 2412	España
T4	TERRITORIO 2398 2404	Madrid
T5	TERRITORIO 2392 2397	28036
T6	CALLE 2365 2391	c/ del Abedul 5-7, 2º dcha
T7	NOMBRE_PERSONAL_SANITARIO 303 326	Ignacio Navarro Cuéllar
T8	NOMBRE_PERSONAL_SANITARIO 2341 2364	Ignacio Navarro Cuéllar
T9	EDAD_SUJETO_ASISTENCIA 389 396	70 años
T10	ID_TITULACION_PERSONAL_SANITARIO 334 345	28 28 70973
T11	FECHAS 282 292	12/12/2016
T12	SEXO_SUJETO_ASISTENCIA 261 262	H
T13	EDAD_SUJETO_ASISTENCIA 247 254	70 años
T14	PAIS 233 239	España
T15	TERRITORIO 166 171	28016
T16	TERRITORIO 154 160	Madrid
T17	CALLE 107 130	Calle Miguel Benitez 90
T18	ID_ASEGURAMIENTO 82 93	26 63514095
T19	ID_SUJETO_ASISTENCIA 68 74	368503
T20	NOMBRE_SUJETO_ASISTENCIA 49 61	Rivera Bueno
T21	NOMBRE_SUJETO_ASISTENCIA 29 36	Ernesto`

More information for annotation guidelines can be found here: http://temu.bsc.es/meddocan/index.php/annotation-guidelines/

__File format of the data:__

The MEDDOCAN corpus is distributed in plain text in UTF8 encoding, where each clinical case is stored as a single file, while PHI annotations are released in the popular BRAT format, which makes visualization of results straightforward. 

__Dataset__

Link: http://temu.bsc.es/meddocan/index.php/data/
The data is provided in Brat and XML formats. For the purpose of this project, we are using the brat format.

● Training: 500 clinical cases (released)
● Development: 250 clinical case (scheduled release - April 4)
● Test set with the background set is composed of at least 2,500 clinical case (scheduled release -
April 29)

Since the actual test data will be made available on April 29, for building our model and evaluation we have
put 99 clinical files aside each from the training data and ________ clinical files from the development data.

New data distribution:
1. Training: 401 clinical cases
2. Development:  clinical cases
3. Testing:  clinical cases


