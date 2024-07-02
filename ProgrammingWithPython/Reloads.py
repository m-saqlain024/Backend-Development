# import Sample1
# import Sample1
# import Sample1
# import Sample1
# import Sample1   this whole will imports once 


# but using importlib 

import importlib
import FileChanges
import Sample1

# importlib.reload(Sample1)
# importlib.reload(Sample1)
# importlib.reload(Sample1)
# importlib.reload(Sample1)
# importlib.reload(Sample1)
# importlib.reload(Sample1)



def changes():
    try:
        importlib.reload(FileChanges)
        FileChanges.print_changes()
    except:
        pass


for i in range(5):
    changes()
    input("Hit enter to relaod the changes ")