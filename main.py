from typing import List, Tuple, Dict
import json


def calculate_panels(panel_width: int|float, panel_height: int|float, 
                    roof_width: int|float, roof_height: int|float) -> int:
    
    # Implementa acá tu solución

#-- Nueva solución (recursividad) --#
    panels_count = 0

    # Orientación vertical del panel
    if panel_height <= roof_height and panel_width <= roof_width:
        vertical_panels = roof_height // panel_height
        horizontal_panels = roof_width // panel_width
        total_panels = vertical_panels * horizontal_panels
        total_panels += calculate_panels(panel_width=panel_width, panel_height=panel_height, roof_height=roof_height,
                                         roof_width= roof_width % panel_width)
        total_panels += calculate_panels(panel_width=panel_width, panel_height=panel_height, roof_width=roof_width,
                                         roof_height=roof_height % panel_height)
        panels_count += total_panels

    # Orientación horizontal del panel
    if panel_height <= roof_width and panel_width <= roof_height:
        vertical_panels = roof_height // panel_width
        horizontal_panels = roof_width // panel_height
        total_panels = vertical_panels * horizontal_panels
        total_panels += calculate_panels(panel_width=panel_width, panel_height=panel_height, roof_height=roof_height,
                                         roof_width= roof_width % panel_height)
        total_panels += calculate_panels(panel_width=panel_width, panel_height=panel_height, roof_width=roof_width,
                                         roof_height=roof_height % panel_width)
        panels_count = max(total_panels, panels_count)
    return panels_count

def run_tests() -> None:
    with open('test_cases.json', 'r') as f:
        data = json.load(f)
        test_cases: List[Dict[str, int]] = [
            {
                "panel_w": test["panelW"],
                "panel_h": test["panelH"],
                "roof_w": test["roofW"],
                "roof_h": test["roofH"],
                "expected": test["expected"]
            }
            for test in data["testCases"]
        ]
    
    print("Corriendo tests:")
    print("-------------------")
    
    for i, test in enumerate(test_cases, 1):
        result = calculate_panels(
            test["panel_w"], test["panel_h"], 
            test["roof_w"], test["roof_h"]
        )
        passed = result == test["expected"]
        
        print(f"Test {i}:")
        print(f"  Panels: {test['panel_w']}x{test['panel_h']}, "
              f"Roof: {test['roof_w']}x{test['roof_h']}")
        print(f"  Expected: {test['expected']}, Got: {result}")
        print(f"  Status: {'✅ PASSED' if passed else '❌ FAILED'}\n")


def main() -> None:
    print("🐕 Wuuf wuuf wuuf 🐕")
    print("================================\n")
    
    run_tests()


if __name__ == "__main__":
    main()


#-- Solución anterior --#
# def calculate_panels(panel_width: int|float, panel_height: int|float, 
#                     roof_width: int|float, roof_height: int|float) -> int:

    # if panel_height <= 0 or panel_width <= 0 or roof_height <= 0 or roof_width <= 0:
    #     return 0
    
    # if panel_height < panel_width:
    #     p_height = panel_width
    #     p_width = panel_height
    # else:
    #     p_height = panel_height
    #     p_width = panel_width

    # if roof_height < roof_width:
    #     roof_height = roof_width
    #     roof_width = roof_height
    # else:
    #     roof_height = roof_height
    #     roof_width = roof_width

    # panel_area = p_height * p_width
    # nro_paneles = 0

    # while p_height <= roof_height and p_width <= roof_width or p_height <= roof_width and p_width <= roof_height:
    #     if p_height <= roof_height and p_width <= roof_width:
    #         roof_sub_area = p_height * roof_width
    #         nro_paneles += roof_sub_area // panel_area
    #         roof_height = roof_height - p_height
    #     else:
    #         roof_sub_area = p_width * roof_width
    #         nro_paneles += roof_sub_area // panel_area
    #         roof_height = roof_height - p_width
    # return nro_paneles
