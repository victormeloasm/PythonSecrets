import secrets
import math

# Function to perform the Miller-Rabin primality test
def is_prime_miller_rabin(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True

    # Determine r and s such that n - 1 = 2^r * s
    s = n - 1
    r = 0
    while s % 2 == 0:
        s //= 2
        r += 1

    # Witness loop
    for _ in range(k):
        a = secrets.randbelow(n - 1) + 1  # Random witness between 1 and n - 1
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False  # Not prime
    return True

# Function to generate a prime number of a specific bit length using Miller-Rabin
def generate_prime_miller_rabin(bit_length):
    while True:
        potential_prime = int(secrets.token_hex(bit_length // 4), 16)
        if is_prime_miller_rabin(potential_prime):
            return potential_prime

# Function to find the greatest common divisor (GCD)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Function to find the modular multiplicative inverse
def mod_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi // e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_phi == 1:
        return d + phi

# Generate random prime numbers p and q using Miller-Rabin
bit_length = 128  # Change this to the desired bit length (e.g., 2048 for real RSA)
p = generate_prime_miller_rabin(bit_length)
q = generate_prime_miller_rabin(bit_length)

# Calculate n (modulus)
n = p * q

# Calculate the totient of n (phi)
phi = (p - 1) * (q - 1)

# Choose a public exponent e
e = 65537  # Commonly used value for e (Fermat's Little Theorem)

# Calculate the private exponent d
d = mod_inverse(e, phi)

# The public key consists of (n, e)
public_key = (n, e)

# Convert the numbers to hexadecimal format
p_hex = hex(p)
q_hex = hex(q)
n_hex = hex(n)
phi_hex = hex(phi)
e_hex = hex(e)
d_hex = hex(d)

# Print the generated values in hexadecimal format
print("p (prime number):", p_hex)
print("q (prime number):", q_hex)
print("n (modulus):", n_hex)
print("phi (totient of n):", phi_hex)
print("e (public exponent):", e_hex)
print("d (private exponent):", d_hex)
print("Public Key (n, e):", public_key)
