class AnyType(str):
  """A special class that is always equal in not equal comparisons. Credit to pythongosssss"""
  def __ne__(self, __value: object) -> bool:
    return False
any_type = AnyType("*")
class CYBERPUNKHT:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
                    "Float": ("FLOAT", {
                        "default": 1,
                        "min": -999999,
                        "max": 999999,
                        "step": 0.01,
                        "display": "slider"
                    }),
                },
                "optional": {},
                "hidden": {
                    "output_type": (["float", "int"], {"default": "float"}),
                }
        }
    RETURN_TYPES = (any_type,)
    FUNCTION = "run"
    CATEGORY = "2🐕/CYBERPUNK"
    INPUT_IS_LIST = False
    OUTPUT_IS_LIST = (False,)
    def run(self, Float, output_type="float"):
        processed_value = round(Float, 10)
        print(f"CYBERPUNKHT: Float={Float}, output_type={output_type}, processed_value={processed_value}")
        if output_type == "int":
            scaled_number = int(round(processed_value))
            print(f"CYBERPUNKHT: Converting to int: {scaled_number}")
        else:
            scaled_number = float(processed_value)
            print(f"CYBERPUNKHT: Keeping as float: {scaled_number}")
        return (scaled_number,)
NODE_CLASS_MAPPINGS = {
    "CYBERPUNKHT": CYBERPUNKHT
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "CYBERPUNKHT": "CYBERPUNKHT"
}
