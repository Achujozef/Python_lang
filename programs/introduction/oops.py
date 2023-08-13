class students:
    clg="Brototype"

    def __init__(self,name,group) :
        self.name=name
        self.group=group

    def display(self):
        print(
            'Name :',self.name,
            "Group : ",self.group,
            "Collage : ",self.clg
        )

class teacher(students):
    pass

std1=teacher('Achu',"IT")
std1.display()


