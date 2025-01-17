# Révision du cours de programmation 1 et compléments d'information

## Les types de bases

### Entiers

 Type | Nombre d'octets | Minimum | Maximum | Notes 
 --|--|--|--|--
 short | 2 octets | -32768 | 32767 |
 ushort | 2 octets | 0 | 65535 |
 int | 4 octets | -2 147 483 648 | 2 147 483 647 |
 uint | 4 octets | 0 | 4 294 967 295 |
 long | 8 octets | 9 223 372 036 854 775 808 | 9 223 372 036 854 775 807 |
 ulong | 8 octets | 0 | 18 446 744 073 709 551 615 |


### Virgules
 Type | Nombre d'octets | Minimum | Maximum | precision 
--|--|--|--|--
float | 4 octets | ±1.5 x 10^−45 | ±3.4 x 10^38	| ~6-9 nombres 	
double | 8 octets | ±5.0 × 10^−324 | ±1.7 × 10^308 | ~15-17 nombres 
decimal | 16 octets | ±1.0 x 10^-28 | ±7.9228 x 10^28 | 28-29 nombres 
   
### Logiques
 Type | Nombre d'octets | Valeurs
 --|--|--
 bool | 1 octet | true/false	

### Textuels
 Type | Nombre d'octets | Notes
 --|--|--
 char | 2 octets | 1 caractère | Valeurs de 0 à 65 535 | 
 string | 0 à 2,147,483,647 x 2 octets (char) |  2 147 483 647 caractères

### Binaires
 Type | Nombre d'octets | Notes
 --|--|--
 byte | 1 octets | Valeurs de 0 à 255
 sbyte | 1 octet | Valeurs de -128 à 127 

## Les structures de controle

### if

``` c# title="simple if"
if (condition) 
{  
    // Bloc de code à executer si la condition retourne "true"  
}  
else if (condition 2)  
{ 
    /* bloc de code 2 */
}
else
{
    /*bloc de code 3*/
}
```

### for


``` c# title="simple for"
   for (affirmation 1; affirmation 2; affirmation 3)  
   {  
      // Bloc de code à executer si la condition retourne "true"  
   }  
```
  

* Affirmation 1 est exécuté (une fois) avant l'exécution du bloc de code.  
* Affirmation 2 définie la condition pour que le bloc soit exécuté.  
* Affirmation 3 est exécuté (chaque fois) après que le bloc de code soit exécuté.  

### while
### do while
### foreach