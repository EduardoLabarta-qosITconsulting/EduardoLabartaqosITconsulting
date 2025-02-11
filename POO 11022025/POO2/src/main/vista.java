package main;

import modelo.Direccion;
import modelo.Estudiante;
import modelo.Persona;
import modelo.Profesor;
import modelo.Trabajador;

public class vista {
    public static void main(String[] args) {
        // Persona(); //Ejc1: Creacion de una clase basica
        // EqualsPersona(); //Ejc2: Uso metodo equals
        // HerenciaBasica(); //Ejc3:Uso de la herencia basica
        // Estudiar();//Ejc4: Uso del this y super
        // Interfaces();// Ejc5: Uso interfaces
        // Polimorfismo(); // Ejc6: Implementacion del poliformismo
        // ComposicionEncapsulamiento();// Ejc7: Uso de la composicion y encapsulamiento
        

    }


    /*
     * private static void ComposicionEncapsulamiento() {
     * Direccion direccion = new Direccion("Calle Estrella",
     * "Sanlucar de Barrameda", "11540");
     * Persona persona1 = new Persona(18, "Eduardo", direccion);
     * 
     * persona1.mostrarDireccion();
     * }
     */

    /*
     * private static void Polimorfismo() {
     * Persona[] personas = new Persona[3];
     * personas[0] = new Persona(20, "Juan");
     * personas[1] = new Estudiante(19, "Eduardo", "Ingieneria Informatica");
     * personas[2] = new Profesor(25, "Jesus", "Matematicas");
     * 
     * for(int x=0; x<personas.length;x++){
     * personas[x].mostrarInformacion();
     * }
     * 
     * 
     * }
     */

    /*
     * private static void Interfaces() {
     * Profesor profesor1 = new Profesor(25, "Jesus", "Matematicas");
     * profesor1.trabajar();
     * }
     */

    /*
     * private static void Estudiar() {
     * Estudiante persona1 = new Estudiante(18, "Eduardo",
     * "Ingieneria Informatica");
     * System.out.println(persona1.getNombre() + " esta estudiando " +
     * persona1.getCarrera());
     * }
     */

    /*
     * private static void HerenciaBasica() {
     * Estudiante persona1 = new Estudiante(18, "Eduardo",
     * "Ingieneria Informatica");
     * System.out.println(persona1.getEdad());
     * System.out.println(persona1.getNombre());
     * System.out.println(persona1.getCarrera());
     * }
     */

    /*
     * private static void EqualsPersona() {
     * Persona persona1 = new Persona(18, "Eduardo");
     * Persona persona2 = new Persona(18, "Eduardo");
     * 
     * System.out.println(persona1.equals(persona2));
     * }
     */

    /*
     * private static void Persona() {
     * Persona persona1 = new Persona(18, "Eduardo");
     * System.out.println(persona1.getEdad());
     * System.out.println(persona1.getNombre());
     * }
     */

}
