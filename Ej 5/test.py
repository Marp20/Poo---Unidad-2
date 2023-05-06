from PlanAhorro import PlanAhorro
from menu import menu



def test_program(lista):
    # Test option 1
    for plan in lista:
        assert plan.get_valorCuotas() == float((plan.get_valor() / plan.get_cuotas()) + plan.get_valor() * 0.10)
        plan.set_valor(500000)
        assert plan.get_valor() == 500000
    
    # Test option 2
    filtered_plans = []
    for plan in lista:
        if plan.get_valorCuotas() < 50000:
            filtered_plans.append(plan)
    assert len(filtered_plans) == 2
    assert filtered_plans[0].get_codigo() == 2
    
    # Test option 3
    expected_monto = lista[1].get_cuotaspagas() * lista[1].get_valorCuotas()
    assert expected_monto == 12055.0
    
    # Test option 4
    lista[0].set_cuotaspagas(10)
    assert lista[0].get_cuotaspagas() == 10