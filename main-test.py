from main import Basic

def TestBasic():
    assert Basic(2, 3) == 5
    assert Basic(5, 5) == 10
    assert Basic(6, 6) == 13
    print("El aplicativo pasa la integracion, pasa a la entrega o despliegue.")

if __name__ == '__main__':
    TestBasic()