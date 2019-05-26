package component;


public enum ResultConvertor {
    PASS( 1 ),
    FAIL( 2 );


    ResultConvertor(final int s) {
        this.status = s;

    }

    private int status;

    public int getStatus() {
        return status;
    }
}
