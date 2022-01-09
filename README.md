# DNI

Escribe un programa que dado un número de DNI obtenga la letra del NIF. La letra correspondiente a un DNI se calcula mediante el siguiente algoritmo: 
- Se obtiene el resto de dividir el número de DNI entre 23. 
- El número resultante indica la posición de la letra correspondiente a ese DNI en la siguiente cadena:

Tabla de asignación

	 	 	
No se utilizan las letras: I, Ñ, O, U.
La “I” y la “O” se evitan para evitar confusiones con otros caracteres, como “1”, “l” ó “0”.

Construye el programa utilizando un vector para almacenar cada una de las letras de la tabla anterior. Luego utiliza un diccionario para almacenar la tabla de asignación. Divide el código mediante una capa de lógica y una capa de acceso a datos para que los cambios en la estructura de datos utilizada (vector o diccionario) no supongan modificaciones en el código correspondiente a la lógica. Observa en la figura la arquitectura en tres capas de la aplicación
