

# Parent class
class Massage:
    technique_name = "Unknown"
    year_created = 0
    country_of_origin = "Unknown"
    pressure_level = "Unknown"
    benefits = "Increased circulation"
    hands_on = True

    # Parent method
    def information(self):
        msg = "\nTechnique Name: {}, \nYear Created: {}, \nCountry of Origin: {}, \nPressure Level: {}, \nBenefits: {}, \nHands On: {}".format(self.technique_name,self.year_created,self.country_of_origin,self.pressure_level,self.benefits,self.hands_on)
        return msg


# Child class instance
class Effleurage(Massage):
    technique_name = "Effleurage"
    year_created = 1830
    country_of_origin = "Sweden"
    pressure_level = "Light"
    benefits = "Increased circulation"
    hands_on = True
    additional_benefits = "Added blood flow and nutrients to the skin"
    uniqueness = "Long, soothing, circular movements"

    # child class method
    def soothing(self):
        msg = "\nAdditional Benefits: {}, \nWhat makes this technique unique: {} \n\nThis is a great technique for warming up the muscles, stimulating venous and lymph return, \nand increasing relaxation before deeper techniques.".format(self.additional_benefits,self.uniqueness)
        return msg


# Another child class instance
class Myofascial_Release(Massage):
    technique_name = "Myofascial Release"
    year_created = 1981
    country_of_origin = "USA"
    pressure_level = "Light"
    benefits = "Eliminating pain"
    hands_on = True
    additional_benefits = "Restoring optimum performance of the body"
    uniqueness = "Light traction is applied"

    # child class method
    def healing(self):
        msg = "\nAdditional Benefits: {}, \nWhat makes this technique unique: {} \n\nThis technique offers incredible long-term healing effects!".format(self.additional_benefits,self.uniqueness)
        return msg



if __name__ == "__main__":
    effleurage = Effleurage()
    print(effleurage.information())
    print(effleurage.soothing())

    myofascial = Myofascial_Release()
    print(myofascial.information())
    print(myofascial.healing())

        

    
    
