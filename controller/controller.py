from usecases.configusecases import ConfigUseCases
from services.meliapiservices import MeLiApiService
import time
import csv

class HubController:
    def __init__(self):
        pass

    def printCsv(self, products = []):
        with open('file.csv', 'w', newline='') as file:
            fieldnames   = ['Description', 'Price', 'Link']
            writer      = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for product in products:
                writer.writerow({ 'Description': str(product['description'], 'utf-8'), 'Price': int(product['price']), 'Link': product['permalink' ]})
                print("{},{},{}".format(str(product['description'], 'utf-8'), float(product['price']), str(product['permalink'])))
            

    def startMainLoop(self, configDict):
        iteration = 1
        while 1==1:
            useCases = ConfigUseCases()
            useCases.create(configDict)
            print("#{} Main HUB loop started".format(iteration))
            print("# Config HUB -- {}".format(useCases.toString()))

            print("# Starting service - sites")
            servicesApi = MeLiApiService()
        #    
            if configDict["services"]["sites"] == True:
                response = servicesApi.sites(useCases)
                print("# Service HUB -- {}".format(response))
        #   
            if configDict["services"]["categories"] == True:
                response = servicesApi.categories(useCases)
                print("# Service HUB -- {}".format(response))
        # 
            if configDict["services"]["catalog_listing"] == True:
                print("# Starting service - catalog listing")
                response = servicesApi.catalogListByQuery(useCases)
                print("# Service HUB -- {}".format(response))
        #
            if configDict["services"]["csv_file"] == True:
                print("# Generating CSV file")
                response = servicesApi.catalogListByQuery(useCases)
                self.printCsv(response) # Geração de arquivo csv
            #                    
            iteration = iteration + 1
            time.sleep(5)