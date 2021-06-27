public class Pair<K, V> {
    private K x;
    private V y;

    public Pair(K x, V y) {
        this.x = x;
        this.y = y;
    }

    public K getX() {
        return this.x;
    }

    public V getY() {
        return this.y;
    }

    @Override
    @SuppressWarnings("unchecked")
    public boolean equals(Object o) {
        if (!(o instanceof Pair)) {
            return false;
        }
        Pair<K, V> p = (Pair<K, V>) o;
        return this.x.equals(p.x) && this.y.equals(p.y);
    }

    @Override
    public int hashCode() {
        long l = x.hashCode() * 2654435761L; 
        return (int)l + (int)(l >>> 32) + y.hashCode();
    }

    public static <K, V> Pair<K, V> createPair(K x, V y) {
        return new Pair<K, V>(x, y);
    }
}