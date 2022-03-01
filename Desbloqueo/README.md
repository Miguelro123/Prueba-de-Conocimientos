Tienes n número de cajas cerradas frente a ti.
Cada caja está numerada secuencialmente de 0 a “n – 1” y cada cuadro puede contener
claves a las otras cajas.
Escriba un método “desbloqueo” que determine si se pueden abrir todas las casillas.

• Prototipo: def desbloqueo(caja)
• caja es una lista de listas.
• Una caja es una lista de llaves ejm. [2,8,6] que abren otras cajas.
• Puedes asumir que todas las llaves serán enteros positivos.
• Puede haber cajas sin llaves.
• La primera caja “caja[0]” está desbloqueada
• “Return True” Si todas las cajas se pueden abrir, o si no “Return False”

Cree un archivo main.py con el siguiente contenido
#!/usr/bin/python3

desbloqueo = __import__('0-lockcaja').desbloqueo

caja = [[1], [2], [3], [4], []]
print(desbloqueo(caja))

caja = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(desbloqueo(caja))

caja = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(desbloqueo(caja))

Luego de crear su método el resultado de ejecutar el main deberá ser el siguiente:
$./main_0.py
True
True
False
