from main import Basic

def TestBasic():
    assert Basic(3, 3) == 6
    print("El aplicativo pasa la integracion, pasa a la entrega o despliegue.")

if __name__ == '__main__':
    TestBasic()