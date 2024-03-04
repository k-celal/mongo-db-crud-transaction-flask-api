# User Management System

Bu basit web uygulaması, kullanıcı ekleme, listeleme, güncelleme ve silme işlemlerini gerçekleştirebilen bir kullanıcı yönetim sistemini içerir. Flask ve MongoDB kullanılarak oluşturulmuştur.

## Kurulum

1. Bu projeyi klonlayın:

    ```bash
    git clone [repository_link](https://github.com/k-celal/mongo-db-crud-transaction-flask-api/)
    ```

2. Proje dizinine gidin:

    ```bash
    cd mongo-db-crud-transaction-flask-api
    ```

3. Gerekli Python paketlerini yükleyin:

    ```bash
    pip install -r requirements.txt
    ```
4. MongoDB veritabanında `UserData` adında bir veritabanı oluşturun ve içine `Users` adında bir koleksiyon ekleyin. 

5. Flask uygulamasını başlatın:

    ```bash
    python main.py
    ```

6. Tarayıcınızda [http://127.0.0.1:5000](http://127.0.0.1:5000) adresine gidin.

## Kullanım

- **Add User (Kullanıcı Ekle)**: Sağ üst köşede bulunan formu kullanarak yeni bir kullanıcı ekleyebilirsiniz. Her kullanıcının bir ID ve bir kullanıcı adı vardır.

- **Delete User (Kullanıcı Sil)**: Her kullanıcının yanında bulunan "Delete" düğmesine tıklayarak bir kullanıcıyı silebilirsiniz.

- **Update User (Kullanıcı Güncelle)**: Her kullanıcının yanında bulunan "Update" düğmesine tıklayarak bir kullanıcının adını güncelleyebilirsiniz.

## Notlar

- Bu uygulamayı kullanarak, MongoDB veritabanına bağlanmanız ve kullanıcı verilerini saklamanız gerekmektedir. Bunun için MongoDB'de bir `UserData` veritabanı ve içinde `Users` koleksiyonu oluşturmalısınız. Kendi MongoDB bağlantı URL'nizi `main.py` dosyasında belirtmelisiniz.

## Teknolojiler

- Flask: Web uygulaması oluşturmak için kullanılan Python web framework'ü.
- MongoDB: NoSQL veritabanı olarak kullanılan MongoDB, kullanıcı verilerini saklamak için kullanılır.
- 
</Good coding with MuyuX 👨‍💻>
