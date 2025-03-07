# Define an immutable bytes object
data_bytes = bytes([65, 66, 67, 68])  # ASCII values for A, B, C, D
print("Bytes:", data_bytes)

# Define a mutable bytearray from the bytes object
data_bytearray = bytearray(data_bytes)
print("Original Bytearray:", data_bytearray)

# Modify the bytearray
data_bytearray[0] = 97  # Changing 'A' (65) to 'a' (97)
print("Modified Bytearray:", data_bytearray)

# Create a memoryview on the bytearray
data_memoryview = memoryview(data_bytearray)

# Access and modify data via memoryview
print("Memoryview Before:", data_memoryview[:].tobytes())
data_memoryview[1] = 98  # Changing 'B' (66) to 'b' (98)
print("Memoryview After:", data_memoryview[:].tobytes())

# Final state of bytearray
print("Final Bytearray:", data_bytearray)