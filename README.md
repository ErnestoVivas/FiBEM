# FiBEM
FiBEM - The Fiware Building Entities Manager

## About
FiBEM is a tool to easily set up entities and relationships that describe
building energy systems and to automatically post them to a real FIWARE application.

Entities and relationships are described by the FiBEM model (Fiware Brick Entities Model),
which uses the Brick Schema ontology to provide semantics for the entity-relationship model.


Following functions can be performed by FiBEM:

Creating entity-relationship models:
* Create entities by adding entities manually, entity id's may be set manually if desired.
* Create relationships between entities manually
* Set relationships between entities automatically
* Get entities and relationships automatically from an FMU model
* delete entities or relationships
* save a created entity-relationship model
* import a before saved entity-relationship model

Using entity-relationship models:
* Post the created model to a FIWARE application such that it serves real-life applications
* Export the ontology of the model (saves a turtle file that can be visualized)
* Export the entity-relationship model to a JSON file


FiBEM is designed to be extendable and you are welcome to add more functions or
extend the fibem model.


## Installation and usage

### Executing FiBEM
FiBEM uses a conda environment to run. After cloning the repository open a terminal
and navigate to the main folder of FiBEM. Here you will find the file "fibem_env.yml".
Create the conda environment:
´´´
conda env create -f fibem_env.yml
´´´

After the conda environment has been created activate it before executing FiBEM:
´´´
conda activate fibem_env
´´´

Once the environment is activate, navigate to FiBEM/src and execute main.py:
´´´
(fibem_env) PS C:\..<Path>..\FiBEM\src> python main.py
´´´

That's it. If you do not want to use the conda environment, make sure your local
python environment has the packages listed in the fibem_env.yml file installed.
Then navigate to FiBEM/src and execute python main.py.


### Posting to FIWARE
FiBEM itself works without FIWARE. You can create, import, save and export
entity-relationship models of building energy system without a FIWARE application
running. If you want to post the model to FIWARE, make sure the target machine
has the following FIWARE services running, otherwise an error will be thrown:
- FIWARE Orion Context Broker accessible on port 1026
- MongoDB
- IoT Agent for JSON

The communication with devices is designed to work over MQTT.
