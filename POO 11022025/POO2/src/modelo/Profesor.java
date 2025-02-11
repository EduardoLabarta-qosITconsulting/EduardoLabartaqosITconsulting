package modelo;

public class Profesor extends Persona implements Trabajador{


    private String especialidad;

    

    public Profesor(int edad, String nombre, Direccion Direccion,String especialidad) {
        super(edad, nombre,Direccion);
        this.especialidad = especialidad;
    }

    public void trabajar(){
        System.out.println(getNombre()+" esta especializado en "+getEspecialidad());
    }

    public void mostrarInformacion(){
        System.out.println("Su nombre es "+getNombre()+" con "+getEdad()+" años y su especialidad es "+getEspecialidad());
    }

    public String getEspecialidad() {
        return especialidad;
    }

    public void setEspecialidad(String especialidad) {
        this.especialidad = especialidad;
    }


   


}
