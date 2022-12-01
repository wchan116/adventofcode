import java.io.BufferedReader
import java.io.FileNotFoundException
import java.io.FileReader
import java.lang.NullPointerException

class Utils {
    companion object {
        fun readFromFileIntoList(file: String): List<String>? {
            try {
                BufferedReader(FileReader(file)).use { br ->
                    return br.readLines()
                }
            } catch (e: FileNotFoundException) {
                println("File Not Found!")
            }
            return null
        }

        fun readFromFile(file: String): String? {
            try {
                BufferedReader(FileReader(file)).use { br ->
                    return br.readText()
                }
            } catch (e: FileNotFoundException) {
                println("File Not Found!")
            } catch (e: NullPointerException) {
                // eof
            }
            return null
        }
    }
}