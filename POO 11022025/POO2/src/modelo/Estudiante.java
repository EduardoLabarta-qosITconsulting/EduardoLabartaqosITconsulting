package modelo;

public class Estudiante extends Persona {


    private String carrera;

    public Estudiante(int edad, String nombre,Direccion Direccion ,String carrera) {
        super(edad, nombre,Direccion);
        this.carrera = carrera;
    }

    public void mostrarInformacion(){
        System.out.println("Su nombre es "+getNombre()+" con "+getEdad()+" años y su carrera es "+getCarrera());
    }

    @Override
    public String toString() {
        return "Estudiante [carrera=" + carrera + ", getEdad()=" + getEdad() + ", getNombre()=" + getNombre() + "]";
    }

    public String getCarrera() {
        return carrera;
    }

    public void setCarrera(String carrera) {
        this.carrera = carrera;
    }

    

}
