import java.io.BufferedReader
import java.io.FileNotFoundException
import java.io.FileReader
import java.lang.NullPointerException

class Utils {
    companion object {
        fun readFromFile(file: String): List<String> {
            val inp: MutableList<String> = ArrayList()
            try {
                BufferedReader(FileReader(file)).use { br ->
                    var line: String
                    while (br.readLine().also { line = it } != null) {
                        inp.add(line)
                    }
                }
            } catch (e: FileNotFoundException) {
                println("File Not Found!")
            } catch (e: NullPointerException) {
                // eof
            }
            return inp
        }
    }
}