from main import Basic

def TestBasic():
    assert Basic(2, 3) == 5
    assert Basic(5, 5) == 11
    print("El aplicativo pasa la integracion, pasa a la entrega o despliegue.")

if __name__ == '__main__':
    TestBasic()