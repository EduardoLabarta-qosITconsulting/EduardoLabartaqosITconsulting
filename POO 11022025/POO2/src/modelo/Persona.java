package modelo;
public class Persona {

    private int edad;
    private String nombre;
    private Direccion direccion;

    public Persona(int edad, String nombre, Direccion direccion) {
        this.edad = edad;
        this.nombre = nombre;
        this.direccion = direccion;
    }

    public int getEdad() {
        return edad;
    }

    public void setEdad(int edad) {
        this.edad = edad;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

   public void mostrarDireccion(){
    System.out.println("Direccion de "+getNombre()+" es "+getDireccion());
   }

    public void mostrarInformacion(){
        System.out.println("Su nombre es "+getNombre()+" con "+getEdad()+" años");
    }

    @Override
    public int hashCode() {
        final int prime = 31;
        int result = 1;
        result = prime * result + edad;
        result = prime * result + ((nombre == null) ? 0 : nombre.hashCode());
        return result;
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj)
            return true;
        if (obj == null)
            return false;
        if (getClass() != obj.getClass())
            return false;
        Persona other = (Persona) obj;
        if (edad != other.edad)
            return false;
        if (nombre == null) {
            if (other.nombre != null)
                return false;
        } else if (!nombre.equals(other.nombre))
            return false;
        return true;
    }


    





    @Override
    public String toString() {
        return "Persona [edad=" + edad + ", nombre=" + nombre + ", direccion=" + direccion + "]";
    }

    public Direccion getDireccion() {
        return direccion;
    }

    public void setDireccion(Direccion direccion) {
        this.direccion = direccion;
    }

    
}
