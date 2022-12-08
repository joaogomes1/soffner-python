# 8. Escreva um programa que desenhe uma tela de abertura com a logomarca da empresa "ACME" (usar caracteres da Tabela ASCII).

##### ##### #   # #####
#   # #     ## ## #
##### #     # # # ####
#   # #     #   # #
#   # ##### #   # #####

# linha 1
# exemplo: 51 (5 hashtags, 1 espaço)
# 51 51 13 11 5

print(5 * '#', end='')
print(' ', end='')

print(5 * '#', end='')
print(' ', end='')

print('#', end='')
print(3 * ' ', end='')

print('#', end='')
print(' ', end='')

print(5 * '#')

# linha 2
# 13 11 15 21 21 1

print('#', end='')
print(3 * ' ', end='')

print('#', end='')
print(' ', end='')

print('#', end='')
print(5 * ' ', end='')

print(2 * '#', end='')
print(' ', end='')

print(2 * '#', end='')
print(' ', end='')

print('#')

# linha 3
# 51 15 11 11 11 4

print(5 * '#', end='')
print(' ', end='')

print('#', end='')
print(5 * ' ', end='')

print('#', end='')
print(' ', end='')

print('#', end='')
print(' ', end='')

print('#', end='')
print(' ', end='')

print(4 * '#')

# linha 4
# 13 11 15 13 11 1

print('#', end='')
print(3 * ' ', end='')

print('#', end='')
print(' ', end='')

print('#', end='')
print(5 * ' ', end='')

print('#', end='')
print(3 * ' ', end='')

print('#', end='')
print(' ', end='')

print('#')

# linha 5
# 13 11 51 13 11 5

print('#', end='')
print(3 * ' ', end='')

print('#', end='')
print(' ', end='')

print(5 * '#', end='')
print(' ', end='')

print('#', end='')
print(3 * ' ', end='')

print('#', end='')
print(' ', end='')

print(5 * '#')
